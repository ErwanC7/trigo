##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## Makefile du 108trigo
##

NAME	=	108trigo

CP		=	cp

CHMOD	=	chmod

all :	$(NAME)

$(NAME) :
	$(CP) sources/main.py ./$(NAME)
	$(CHMOD) +x $(NAME)

clean :
	$(RM) $(NAME)

fclean :
	$(RM) $(NAME)

re :	fclean all

.PHONY :	all clean fclean re
