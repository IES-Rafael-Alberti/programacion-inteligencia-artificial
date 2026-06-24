source /home/ec2-user/anaconda3/etc/profile.d/conda.sh
echo "Starting conda create command for rapidsai env"
conda create --solver=libmamba -n rapids-24.02 -c rapidsai -c conda-forge -c nvidia rapids=24.02 python=3.10 cuda-version=12.0

conda activate rapids-24.02

conda install ipykernel

python -m ipykernel install --user --name rapids-24.02 --display-name rapids-24.02

# si el notebook está abierto cerramos y volvemos a abrir, ya debería permitir usar el kernel


