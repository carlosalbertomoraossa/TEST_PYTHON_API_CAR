FNAME="function"

rm function.zip

python3 -m venv vEnvTemp
source vEnvTemp/bin/activate
pip install -r requirements.txt

cd vEnvTemp/lib/python3.10/site-packages

#find . -maxdepth 1  -type d \( -name "*-info" -o -name "__pycache__" -o -name "tests" \) -exec  rm -rf -f {} \;
zip -r9  ../../../../$FNAME.zip ./

cd ../../../../
rm -rf vEnvTemp


declare -a arr=("lambda_function.py")

for i in "${arr[@]}"
do
    zip -g $FNAME.zip $i
done

zip -gr $FNAME.zip app/