#!/bin/bash

pat_file=$1

while IFS= read -r pat; do
    echo "Pattern -> $pat"
done < "$pat_file"

