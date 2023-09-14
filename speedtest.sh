#!/bin/bash

declare -A write_speeds
declare -A read_speeds

# List of drives to be tested
drives=("HDD1" "HDD2" "HDD3" "HDD_RAID" "SSD1")

# Test write speeds
for drive in "${drives[@]}"
do
    echo "Testing write speed for $drive..."
    result=$(dd if=/dev/zero of=/mnt/$drive/testfile bs=1G count=1 oflag=direct 2>&1)
    rm -f /mnt/$drive/testfile
    speed=$(echo $result | grep -oP '\d+(\.\d+)? MB/s' | grep -oP '\d+(\.\d+)?')
    write_speeds["$drive"]=$speed
    echo "$drive Write Speed: $speed MB/s"
done

# Test read speeds
for drive in "${drives[@]}"
do
    dd if=/dev/zero of=/mnt/$drive/testfile bs=1G count=1 oflag=direct > /dev/null 2>&1
    echo "Testing read speed for $drive..."
    result=$(dd if=/mnt/$drive/testfile of=/dev/null bs=1G count=1 iflag=direct 2>&1)
    rm -f /mnt/$drive/testfile
    speed=$(echo $result | grep -oP '\d+(\.\d+)? MB/s' | grep -oP '\d+(\.\d+)?')
    read_speeds["$drive"]=$speed
    echo "$drive Read Speed: $speed MB/s"
done

# Sort and output the results
echo "Write Speeds from High to Low:"
for speed in $(echo "${write_speeds[@]}" | tr ' ' '\n' | sort -rn)
do
    for drive in "${!write_speeds[@]}"
    do
        if [[ "${write_speeds[$drive]}" == "$speed" ]]
        then
            echo "$drive: $speed MB/s"
            unset write_speeds[$drive]
            break
        fi
    done
done

echo "Read Speeds from High to Low:"
for speed in $(echo "${read_speeds[@]}" | tr ' ' '\n' | sort -rn)
do
    for drive in "${!read_speeds[@]}"
    do
        if [[ "${read_speeds[$drive]}" == "$speed" ]]
        then
            echo "$drive: $speed MB/s"
            unset read_speeds[$drive]
            break
        fi
    done
done