while read -r line; do
    screen -dm bash -c "wget $line"
done < urls.txt