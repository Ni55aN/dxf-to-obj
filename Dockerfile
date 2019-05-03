FROM ikester/blender

ENV PATH="/usr/local/blender:${PATH}"

ENTRYPOINT ["blender", "-noaudio", "--background", "--python"]