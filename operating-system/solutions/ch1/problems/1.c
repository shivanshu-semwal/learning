#include <stdio.h>

#define FILE_LENGTH 100

typedef enum {
  NO_ERROR,
  SRC_DST_MISSING,
  DST_MISSING,
  INVALID_ARGS_NO
} ERROR_LEVEL;

/*
Print the program help to given stream and given error level
 */
void help(FILE *stream, ERROR_LEVEL err) {
  switch (err) {
    case NO_ERROR:
      break;
    case SRC_DST_MISSING:
      fprintf(stderr, "Missing source and destination");
      break;
    case DST_MISSING:
      fprintf(stderr, "Missing destination.");
      break;
    case INVALID_ARGS_NO:
      fprintf(stderr,
              "Extra arguments: only source and destination should be present");
      break;
  }
}

int main(int argc, char const *argv[]) {
  if (argc == 1) {
    help(stderr, SRC_DST_MISSING);
    return 1;
  } else if (argc == 2) {
    help(stderr, DST_MISSING);
    return 2;
  } else if (argc > 3) {
    help(stderr, INVALID_ARGS_NO);
    return 3;
  }

  char *source = argv[1]; // source file
  char *dest = argv[2]; // destination file

  
  // printf(source)
  return 0;
}
