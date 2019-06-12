#!/bin/bash

# loop through challenges
for i in {0..4}
do
    DIR="challenge_$i/submission"
    ZIPFILE="submission$i.zip"
    HASHFILE="submit/hash_$i"

    # Check whether the folder challenge_i/submission has some content
    if [ "$(ls -A $DIR 2> /dev/null)" ]; then
        # Submission folder is not empty

        # Copy over team info
        cp team_info.txt $DIR

        echo "Compressing submission for challenge $i!"
        # Zip the submission
        zip -rq "$ZIPFILE" "$DIR"

        # TODO check file size, don't send if too large

        # Generate a hash of the zip file
        HASH="$(md5sum $ZIPFILE)"
        OLDHASH="$(cat $HASHFILE)"

        # If the hash is stored, the file is already sent:
        # Only send if oldhash != hash
        if [ "$HASH" == "$OLDHASH" ]; then
            echo "These files for challenge $i have already been submitted"
            echo ""
        else
            # Send files and save hash into gitlab CI artifact
            echo "$HASH" > $HASHFILE
            #curl -F 'file=$ZIPFILE' http://submit.robotuprising.fi/upload
            curl -F "file=@$ZIPFILE"  http://lab.robotuprising.fi:8080/upload
            echo ""
            echo "Challenge $i submitted!"
            echo ""
        fi
    else
        echo "No submission for challenge $i"
    fi
done
