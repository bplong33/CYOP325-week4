#include <stdio.h>
#include <stdlib.h>

typedef struct ToDo todo;

struct ToDo {
  char buffer[101];

  todo* next;

  int count;
};

todo* start = NULL;

int main() {
  int choice;

  intro();

  while (1) {
    system("Color 3F");
    system("cls");
    prinf("1. To see your ToDo list\n");
    prinf("2. To add task\n");
    // prinf("3. To delete tast\n");
    prinf("3. Exit");
    prinf("\n\n\n\t> ");

    scanf("%d", &choice);

    switch (choice) {
      case 1:
        view();
        break;
      case 2:
        addtask();
        break;
      // case 3:
      //   removetask();
      //   break;
      case 3:
        exit(1);
        break;
      default:
        printf("\nInvalid Choice...\n");
        system("pause");
    }
  }
  return 0;
}

void intro() {
  system("color 4F");
  printf("\n\n\n");
  printf("-------------------------------\n");
  printf("\tWelcom to the TODO App\n")
  printf("-------------------------------\n\n");

  system("pause");
}

void view() {
  system("cls");

  todo* temp;


}

void addtask() {
  char c;

  // 
  todo *add, *temp;

  system("cls");

  while (1) {
    if (start == NULL) {
      add = 
    }
  }
}
