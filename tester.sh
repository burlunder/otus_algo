#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

_help() {
    echo -en "Usage help:
    \t-d|--test-dir:\t\tdirectory of tests
    \t-s|--script:\t\tscript to test\n"
    exit
}


[ $# == 0 ]  && _help
POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -d|--test-dir)
    TESTDIR="$(realpath ${2})"
    shift # past argument
    shift # past value
    ;;
    -s|--script)
    SCRIPT="$(realpath ${2})"
    shift # past argument
    shift # past value
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    _help
    exit
    ;;
esac
done

# echo "TESTDIR: ${TESTDIR}"
# echo "SCRIPT: ${SCRIPT}"

test_failed=
for file in $(find ${TESTDIR} -name '*.in' ); do
    check_value=$(cat "${file//.in}.out" | tr -d '\r' | tr -d '\n')
    script_value=$(${SCRIPT} ${file})
    # echo -e "script_value: ${script_value}\t\t check_value: ${check_value}"

    if [[ "${script_value}" != "${check_value}" ]]; then
        test_failed=1
        echo -e "---\nTest failed on file $(basename ${file})"
        echo -e "script_value:\t${script_value}"
        echo -e "check_value:\t${check_value}"
        # cat ${file}
    fi
done

[ -z ${test_failed} ] || exit 42
