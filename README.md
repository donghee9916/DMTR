# DMTR
MTR based Racing Vehicle Trajectory Prediction


# Git Command

git 처음 쓰시는 분들, 잘 모르는 분들은 아래 사이트 빠르게 정주행 한번 해주세요  
작업하다가 잘못해서 복구하는거보다 저거 정주행 한번하는게 훨빠름  
https://backlog.com/git-tutorial/kr/intro/intro1_1.html
```
내 컴퓨터 = local / 원격 = origin  
git add : 파일을 Stage로 올리는 과정  
git commit : stage위의 파일을 local 저장소로 등록  
git push : 원격 저장소로 업로드  
git pull : 원격 저장소에서 local로 
git checkout : branch 옮기기 
```

# Git Command order (Branch.ver)
```
git status                                     (current branch)
git pull origin main                           (update local main)
git checkout -b "name of branch"               (new branch)
----- Work -----
git add -A                                     (stage the change)
git commit -m "Description"                    (git commit)
git push origin "name of branch"               (git push)
----- Request for merge branch into main -----
----- merge ------
git checkout main                              (into main branch)
git pull origin main                           (update local main)
git branch -d "name of branch"                 (deleting local branch)
git push origin --delete "name of branch"      (deleting remote branch)
```

# Making Package
```
source /opt/ros/galactic/setup.bash
cd src
ros2 pkg create "PACKAGE_NAME" --build-type ament_python --dependencies rclpy std_msgs
```
setup.py에서 'console scripts'뒤에 노드명과 main문을 작성해주어야 함.
ex) 'console_scripts: [@name_of_node = @folder_name.@code_name@:main]'
ex) 'console_scripts: [@test_node = test_package.test_node@:main]'
