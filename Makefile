style:
	pep8 --exclude thirdparty .
	! grep -r --include \*.hy  '.\{61\}'
	cloc --force-lang=clojure,hy --exclude-dir=thirdparty .