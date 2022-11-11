#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define FILE_SIZE 1024
#define CONFIG_FILE "config.ini"
#define OFFSET_SIZE 19
#define PASSWORD_MAX_LENGTH 30
char *read_file();
int write_file(char *content, char *filename);
int run();
int config();
int help();

extern char **environ;

// function that loops trough the content variable and returns the user in config.ini
char *get_utilizador(){
    char *content = read_file();
    char utilizador[10];
    int i;
    for ( int x = strlen("UTILIZADOR="), i = 0; content[x]!='\n'; i++, x++ )
        if(content[x]!='\n')
            utilizador[i] = content[x];
    char *utilizador_output = malloc(strlen(utilizador)+1);
    strcpy(utilizador_output, utilizador);
    free(content);
    return utilizador_output;
}
// function that loops trough the content less the utilizador variable to fund the password
char *get_pass(){
    char *content = read_file();
    char password[PASSWORD_MAX_LENGTH];
    char *utilizador = get_utilizador();
    for ( int i = 0; i < PASSWORD_MAX_LENGTH; i++ )
        password[i] = ' ';
    for ( int x = strlen(utilizador)+strlen("UTILIZADOR=")+strlen("PASSWORD"), i = 0; content[x]!='\n'; x++)
        if (content[x] != '\n' && content[x] != ' ')
            password[i++] = content[x];
    password[strlen(password)] = '\0';
    free(utilizador);
    free(content);
    char *pass_output = malloc(strlen(password)+1);
    strcpy(pass_output, password);
    return pass_output;
}
// help message in case of mistakes
int help(){
    printf("This program was written in C with the purpose of facilitate the user experience to update it's events to the calendar.\nThe commands you need to understand are just a few and really simple.\nCommands:\n\t- \"run\" it's used to run the python script that contains the code to update the calendar.\n\t- \"config\" it's use to config the password and username to access giae. Note that the password is hidden but it's stored in a file with no protection so be careful with that file.\n\t- \"creds\" this command it's use to get the credentials stored in the config file.\nImportant! Your username is your school number and the password is the one use to access the same.\n");
    return 0;
}
// function used to run the python script
int run(){
    setenv("UTILIZADOR", get_utilizador(), 0);
    setenv("PASSWORD", get_pass(), 0);
    system("python3 main.py");
    return 1;
}
// reads the file configurations file
char *read_file(){
    FILE *file;
    int i=0;
    file = fopen(CONFIG_FILE, "r");
    char *file_content = malloc(sizeof(char)*FILE_SIZE);
    while (!feof(file)){
        file_content[i] = fgetc(file);
        i++;
    }
    file_content[i-1] = '\0';
    fclose(file);
    return file_content;
}
// writes to file with the variable content
int write_file(char *content, char *filename){
    FILE *file;
    file = fopen(filename, "w");
    fprintf(file, "%s", content);
    return 0;
}
// setups the configurations, receiving and writing them to the config file
int config(){
    char username[100];
    char *password;
    printf("\nIntroduce your username: ");scanf("%s", username);
    do{
        password = getpass("Password: ");
    }while(!(PASSWORD_MAX_LENGTH >= strlen(password)));
    char content[50];
    strcpy(content, "UTILIZADOR=");
    strcat(content, username);
    strcat(content, "\nPASSWORD=");
    strcat(content, password);
    content[strlen(content)] = '\n';
    content[strlen(content)+1] = '\0';
    write_file(content, CONFIG_FILE);
    printf("Configurações escritas no ficheiro: %s\n", CONFIG_FILE);
    return 0;
}

int main(int argc, char **argv){
    if (argc < 2)
        printf("\033[0;31mError:\033[0m Too few arguments\nUse --help for more information\n");
    else{
        if(!strcmp(argv[1], "--help") || !strcmp(argv[1],"-h")){ 
            help();
            return 0;
        }
        if (!strcmp(argv[1], "config")){ 
            config();
            return 0;
        }
        if(!strcmp(argv[1], "run")){ 
            run();
            return 0; 
        }
        if(!strcmp(argv[1], "creds")){
            printf("%s\n", get_utilizador());
            printf("%s\n", get_pass());
            return 0;
        }
        printf("\033[0;31mError: \033[0mCommand '%s' Not found\nUse --help for more information\n", argv[1]);
    }
    printf("\a");
    return 0;
}