TARGET = crowded-observation

PYTHON = python
PYTHON_DIR = py
PYTHON_FILES = $(wildcard $(PYTHON_DIR)/*.py)

all: $(TARGET)

test:
	$(PYTHON) $(PYTHON_DIR)/main.py

server:
	node server.js; \
	open http://127.0.0.1:5500/

clean:
	-rm -rf $(PYTHON_DIR)/__pycache__/