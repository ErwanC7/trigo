##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## Makefile du trigo
##

NAME	=	trigo

CP	=	cp

CHMOD	=	chmod

all :	$(NAME)

$(NAME) :
	$(CP) sources/main.py ./$(NAME)
	$(CHMOD) +x $(NAME)

clean :
	$(RM) -r sources/__pycache__/

fclean :
	$(RM) $(NAME)

re : fclean all

.PHONY : all clean fclean re
