# parent_folder=$(dirname,"testops")
# echo "$parent_folder"


# real_path="$(realpath "$0")"
# echo "$real_path"
ini_file="petdata.ini"
config_folder="config"

real_path="$(realpath "$0")"
# echo "$real_path"
base_dir_name="$(dirname $real_path)"
parent_dir="$(dirname $base_dir_name)"
# echo $parent_dir
for file in "$parent_dir/$config_folder";do
    if [ -d "$file" ];then
        for subfile in "$file"/*;do 
            if [ "${subfile##*.}" == "ini" ];then
                echo "$subfile"
            fi    
        done    
    else
        echo "$file"

    fi
done    

