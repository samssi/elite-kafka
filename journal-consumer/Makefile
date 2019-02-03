clean:
	@find . -name '*.py?' -delete
	@find . -name '.cache' -type d | xargs rm -rf
	@find . -name '__pycache__' -type d | xargs rm -rf
	@rm -rf .venv

.env/bin/activate: requirements.txt
	@test -d .env || python3 -m venv .env
	.env/bin/pip install --upgrade pip
	.env/bin/pip install --no-cache-dir -Ur requirements.txt || exit -1
	touch .env/bin/activate

env: .env/bin/activate

