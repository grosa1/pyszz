bugfix_commits_file=$1
conf_file=$2

echo $bugfix_commits_file
echo $conf_file

docker build -t pyszz .

mkdir -p out
mkdir -p temp
docker run \
        -v $PWD/out:/usr/src/app/out \
        -v $bugfix_commits_file:/usr/src/app/bugfix_commits.json \
        -v $conf_file:/usr/src/app/conf.yml \
        pyszz bugfix_commits.json conf.yml
