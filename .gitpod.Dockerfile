FROM gitpod/workspace-full

# Install additional tools if needed
RUN sudo apt-get update && sudo apt-get install -y \
  python3 \
  python3-pip
