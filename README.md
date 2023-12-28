# OrganizeArt.py
This Python script can modify the timestamp of a media file downloaded from Twitter/X. This can assist users who download large batches of pictures (such as artwork, photographs, videos, etc.) and like to organize the typically random filenames by their original upload date & time. This is beneficial to those who enjoy viewing their libraries in a large thumbnail view while being able to sort chronologically.

## Usage
`python OrganizeArt.py directory`

All files in the specified directory named after a valid Twitter ID will have their timestamps replaced. The timestamps are relative to GMT and will display appropriately depending on your system's timezone or locale. The original content of the files themselves will remain untouched.

|Before                                                                                                    |After                                                                                                    |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
|![Before](https://github.com/Anub1sR0cks/OrganizeArt/assets/99109881/d946ab43-36e6-427f-91cd-8c94595d2f96)|![After](https://github.com/Anub1sR0cks/OrganizeArt/assets/99109881/f5fbbb1a-c9f3-4a4e-b418-3268a3a258b3)|

## How It Works
The script works by decoding the *snowflake ID* from the filename's *Twitter ID*, which is a unique 15-character identifier assigned to each Twitter object. The algorithm for extracting the Unix timestamp is as follows:

1) Read the Twitter ID from the filename.
2) Get the snowflake ID by decoding the Twitter ID's base64 string and adding padding if required.
3) Get the first 16 bytes of the snowflake ID (the Unix timestamp).
4) Add the constant Twitter epoch to the result, which is **1288834974657** (or Thursday, November 4, 2010 1:42:54.657 AM).

More information about snowflake IDs: https://en.wikipedia.org/wiki/Snowflake_ID
