FROM python:3.13-slim-trixie

ARG COPILOT_VERSION=1.0.83
ARG DEV_UID=1000
ARG DEV_GID=1000

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        nodejs \
        npm \
    && install -d -m 0755 /etc/apt/keyrings \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        -o /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && printf '%s\n' \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
        > /etc/apt/sources.list.d/github-cli.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends gh \
    && npm install --global --no-audit --no-fund --omit=dev "@github/copilot@${COPILOT_VERSION}" \
    && npm cache clean --force \
    && apt-mark manual nodejs git gh ca-certificates \
    && apt-get purge -y --auto-remove curl npm \
    && rm -rf /var/lib/apt/lists/* /root/.npm

RUN groupadd --gid "${DEV_GID}" dev \
    && useradd --uid "${DEV_UID}" --gid "${DEV_GID}" --create-home --shell /bin/bash dev \
    && install -d -o dev -g dev /workspace /home/dev/.config/gh /home/dev/.copilot \
    && git config --system --add safe.directory /workspace

USER dev
WORKDIR /workspace
CMD ["bash"]
