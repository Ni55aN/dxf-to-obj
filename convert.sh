docker build -t blender .
docker run -v $(pwd):/blender --rm blender /blender/dxf2obj.py $1 $2