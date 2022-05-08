

int strStr(char * haystack, char * needle){
    char* ret;
    ret = strstr(haystack, needle);
    if (ret == NULL){
        return -1;
    }
    int position = ret - haystack;
    return position;
}