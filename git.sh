#!/bin/sh

# yaml불러오기
. ./parse_yaml.sh
eval $(parse_yaml config.yaml "config_")


# git clone $config_fork_url
git remote add $config_nickname https://$config_github_id:$config_github_token@$config_origin_url
git checkout -b $config_branch
git add .
git commit -m $config_commit_msg
git push origin $config_branch

echo -n "If Success to Merged Press yes or not no"
read Suc
if [ ${Suc} -eq "yes" ]; then
    git checkout main
    git pull $config_nickname main
    git push origin main
    git branch -d $config_branch
    git push origin --delete $config_branch
elif [ ${Suc} -eq "no" ]; then
    sudo git reset HEAD^
    exit 0
fi


exit 0