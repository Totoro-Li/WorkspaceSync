#!/bin/bash

declare -A write_speeds
declare -A read_speeds

# Test write speeds
for i in 1 2 3 4
do
    echo "Testing write speed for HDD$i..."
    result=$(dd if=/dev/zero of=/mnt/HDD$i/testfile bs=1G count=1 oflag=direct 2>&1)
    rm -f /mnt/HDD$i/testfile
    speed=$(echo $result | grep -oP '\d+(\.\d+)? MB/s' | grep -oP '\d+(\.\d+)?')
    write_speeds["HDD$i"]=$speed
    echo "HDD$i Write Speed: $speed MB/s"
done

# Test read speeds
for i in 1 2 3 4
do
    dd if=/dev/zero of=/mnt/HDD$i/testfile bs=1G count=1 oflag=direct > /dev/null 2>&1
    echo "Testing read speed for HDD$i..."
    result=$(dd if=/mnt/HDD$i/testfile of=/dev/null bs=1G count=1 iflag=direct 2>&1)
    rm -f /mnt/HDD$i/testfile
    speed=$(echo $result | grep -oP '\d+(\.\d+)? MB/s' | grep -oP '\d+(\.\d+)?')
    read_speeds["HDD$i"]=$speed
    echo "HDD$i Read Speed: $speed MB/s"
done

# Sort and output the results
echo "Write Speeds from High to Low:"
for hdd in $(echo "${write_speeds[@]}" | tr ' ' '\n' | sort -rn)
do
    for hddname in "${!write_speeds[@]}"
    do
        if [[ "${write_speeds[$hddname]}" == "$hdd" ]]
        then
            echo "$hddname: $hdd MB/s"
            unset write_speeds[$hddname]
            break
        fi
    done
done

echo "Read Speeds from High to Low:"
for hdd in $(echo "${read_speeds[@]}" | tr ' ' '\n' | sort -rn)
do
    for hddname in "${!read_speeds[@]}"
    do
        if [[ "${read_speeds[$hddname]}" == "$hdd" ]]
        then
            echo "$hddname: $hdd MB/s"
            unset read_speeds[$hddname]
            break
        fi
    done
done