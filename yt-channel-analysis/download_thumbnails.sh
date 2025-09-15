download_thumbnail() {
    URL="$1"
    OUTPUT_FILENAME=$(echo -n "$URL" | md5sum | awk '{print $1}')
    OUTPUT_DIR="thumbnails"
    echo "$OUTPUT_FILENAME"
    curl "$URL" \
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' \
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8' \
        -H 'Accept-Language: en-US,en;q=0.5' \
        -H 'Accept-Encoding: gzip, deflate, br, zstd' \
        --output "$OUTPUT_DIR/$OUTPUT_FILENAME.webp"
    sleep 1
}

while IFS= read -r line
do
    download_thumbnail "$line"
    echo $line
    echo "-----------------------------"
    # break
done < "thumbnailsurl"
