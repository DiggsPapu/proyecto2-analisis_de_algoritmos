CC = g++
CFLAGS = -std=c++11
PYTHON_INCLUDE = /usr/include/python3.11/
PYTHON_LIB = -lpython3.11

SRCS = divideAndConquer.cpp
OBJS = $(SRCS:.cpp=.o)
EXEC = divideAndConquer

.PHONY: all clean run

all: $(EXEC)

$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) -I$(PYTHON_INCLUDE) $(OBJS) -o $(EXEC) $(PYTHON_LIB)
	./$(EXEC)
	python3 ./divideAndConquer.py

%.o: %.cpp
	$(CC) $(CFLAGS) -I$(PYTHON_INCLUDE) -c $< -o $@

run: $(EXEC)
	./$(EXEC)
	python3 ./divideAndConquer.py

clean:
	rm -f $(OBJS) $(EXEC) basic.png
