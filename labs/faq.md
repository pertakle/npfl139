### TOC: FAQ

### TOCEntry: Install

- _What Python version to use_

  The recommended Python version is **3.11**. This version is used by ReCodEx to
  evaluate your solutions. Minimum required version is Python 3.10.

  You can find out the version of your Python installation using `python3 --version`.

- _Installing to central user packages repository_

  You can install all required packages to central user packages repository using
  `python3 -m pip install --user --no-cache-dir --extra-index-url=https://download.pytorch.org/whl/cu118 npfl139`.

  On Linux and Windows, the above command installs CUDA 11.8 PyTorch build, but you can change `cu118` to:
  - `cpu` to get CPU-only (smaller) version,
  - `cu124` to get CUDA 12.4 build,
  - `rocm6.2.4` to get AMD ROCm 6.2.4 build (Linux only).

  On macOS, the `--extra-index-url` has no effect and the Metal support is
  installed in any case.

  **To update the `npfl139` package later, use `python3 -m pip install --user --upgrade npfl139`.**
- _Installing to a virtual environment_

  Python supports virtual environments, which are directories containing
  independent sets of installed packages. You can create a virtual environment
  by running `python3 -m venv VENV_DIR` followed by
  `VENV_DIR/bin/pip install --no-cache-dir --extra-index-url=https://download.pytorch.org/whl/cu118 npfl139`.
  (or `VENV_DIR/Scripts/pip` on Windows).

  Again, apart from the CUDA 11.8 build, you can change `cu118` on Linux and
  Windows to:
  - `cpu` to get CPU-only (smaller) version,
  - `cu124` to get CUDA 12.4 build,
  - `rocm6.2.4` to get AMD ROCm 6.2.4 build (Linux only).

  **To update the `npfl139` package later, use `VENV_DIR/bin/pip install --upgrade npfl139`.**

- _**Windows** installation_

  - On Windows, it can happen that `python3` is not in PATH, while `py` command
    is – in that case you can use `py -m venv VENV_DIR`, which uses the newest
    Python available, or for example `py -3.11 -m venv VENV_DIR`, which uses
    Python version 3.11.

  - If **MuJoCo environments fail** during construction, make sure the path of
    the Python site packages contains no non-ASCII characters. If it does, you
    can create a new virtual environment in a suitable directory to circumvent
    the problem.

  - If you encounter a problem creating the logs in the `args.logdir` directory,
    a possible cause is that the path is longer than 260 characters, which is
    the default maximum length of a complete path on Windows. However, you can
    increase this limit on Windows 10, version 1607 or later, by following
    the [instructions](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation).

- _**MacOS** installation_

  - If you encounter issues with SSL certificates (_certificate verify failed:
    self-signed certificate in certificate chain_), you probably need to run the
    `Install Certificates.command`, which should be executed after installation;
    see https://docs.python.org/3/using/mac.html#installation-steps.

- _**GPU** support on Linux and Windows_

  PyTorch supports NVIDIA GPU or AMD GPU out of the box, you just need to select
  appropriate `--extra-index-url` when installing the packages.

  If you encounter problems loading CUDA or cuDNN libraries, make sure your
  `LD_LIBRARY_PATH` does not contain paths to older CUDA/cuDNN libraries.

### TOCEntry: MetaCentrum

- _How to apply for MetaCentrum account?_

  After reading the [Terms and conditions](https://docs.metacentrum.cz/en/docs/access/terms),
  you can [apply for an account here](https://docs.metacentrum.cz/en/docs/access/account).

  After your account is created, please make sure that the directories
  containing your solutions are always **private**.

- _How to activate Python 3.11 on MetaCentrum?_

  On Metacentrum, currently the newest available Python is 3.11, which you need
  to activate in every session by running the following command:
  ```
  module add python/3.11.11-gcc-10.2.1-555dlyc
  ```

- _How to install the required virtual environment on MetaCentrum?_

  To create a virtual environment, you first need to decide where it will
  reside. Either you can find a permanent storage, where you have large-enough
  [quota](https://docs.metacentrum.cz/en/docs/access/account), or you can [use scratch
  storage for a submitted job](https://docs.metacentrum.cz/en/docs/computing/infrastructure/scratch-storages).

  TL;DR:
  - Run an interactive CPU job, asking for 16GB scratch space:
    ```
    qsub -l select=1:ncpus=1:mem=8gb:scratch_local=16gb -I
    ```

  - In the job, use the allocated scratch space as the temporary directory:
    ```
    export TMPDIR=$SCRATCHDIR
    ```

  - You should clear the scratch space before you exit using the `clean_scratch`
    command. You can instruct the shell to call it automatically by running:
    ```
    trap 'clean_scratch' TERM EXIT
    ```

  - Finally, create the virtual environment and install PyTorch in it:
    ```
    module add python/3.11.11-gcc-10.2.1-555dlyc
    python3 -m venv CHOSEN_VENV_DIR
    CHOSEN_VENV_DIR/bin/pip install --no-cache-dir --extra-index-url=https://download.pytorch.org/whl/cu118 npfl139
    ```

- _How to run a GPU computation on MetaCentrum?_

  First, read the official MetaCentrum documentation:
  [Basic terms](https://docs.metacentrum.cz/en/docs/computing/concepts),
  [Run simple job](https://docs.metacentrum.cz/en/docs/computing/run-basic-job),
  [GPU computing](https://docs.metacentrum.cz/en/docs/computing/gpu-comput/gpu-job),
  [GPU clusters](https://docs.metacentrum.cz/en/docs/computing/gpu-comput/clusters).

  TL;DR: To run an interactive GPU job with 1 CPU, 1 GPU, 8GB RAM, and 32GB scatch
  space, run:
  ```
  qsub -l select=1:ncpus=1:ngpus=1:mem=8gb:scratch_local=32gb -I
  ```

  To run a script in a non-interactive way, replace the `-I` option with the script to be executed.

  If you want to run a CPU-only computation, remove the `ngpus=1:` from the above commands.

### TOCEntry: AIC

- _How to install required packages on [AIC](https://aic.ufal.mff.cuni.cz)?_

  The Python 3.11.7 is available `/opt/python/3.11.7/bin/python3`, so you should
  start by creating a virtual environment using
  ```
  /opt/python/3.11.7/bin/python3 -m venv VENV_DIR
  ```
  and then install the required packages in it using
  ```
  VENV_DIR/bin/pip install --no-cache-dir --extra-index-url=https://download.pytorch.org/whl/cu118 npfl139
  ```

- _How to run a GPU computation on AIC?_

  First, read the official AIC documentation:
  [Submitting CPU Jobs](https://aic.ufal.mff.cuni.cz/index.php/Submitting_CPU_Jobs),
  [Submitting GPU Jobs](https://aic.ufal.mff.cuni.cz/index.php/Submitting_GPU_Jobs).

  TL;DR: To run an interactive GPU job with 1 CPU, 1 GPU, and 16GB RAM, run:
  ```
  srun -p gpu -c1 -G1 --mem=16G --pty bash
  ```

  To run a shell script requiring a GPU in a non-interactive way, use
  ```
  sbatch -p gpu -c1 -G1 --mem=16G SCRIPT_PATH
  ```

  If you want to run a CPU-only computation, remove the `-p gpu` and `-G1`
  from the above commands.

### TOCEntry: Git

- _Is it possible to keep the solutions in a Git repository?_

  Definitely. Keeping the solutions in a branch of your repository,
  where you merge them with the course repository, is probably a good idea.
  However, please keep the cloned repository with your solutions **private**.

- _On GitHub, do not create a **public** fork with your solutions_

  If you keep your solutions in a GitHub repository, please do not create
  a clone of the repository by using the Fork button – this way, the cloned
  repository would be **public**.

  Of course, if you just want to create a pull request, GitHub requires a public
  fork and that is fine – just do not store your solutions in it.

- _How to clone the course repository?_

  To clone the course repository, run
  ```
  git clone https://github.com/ufal/npfl139
  ```
  This creates the repository in the `npfl139` subdirectory; if you want a different
  name, add it as a last parameter.

  To update the repository, run `git pull` inside the repository directory.

- _How to keep the course repository as a branch in your repository?_

  If you want to store the course repository just in a local branch of your
  existing repository, you can run the following command while in it:
  ```
  git remote add course_repo https://github.com/ufal/npfl139
  git fetch course_repo
  git checkout --track course_repo/master -b BRANCH_NAME
  ```
  This creates a branch `BRANCH_NAME`, and when you run `git pull` in that
  branch, it will be updated to the current state of the course repository.

- _How to merge the course repository updates with your modified branch?_

  If you want to store your solutions in your branch and gradually update this
  branch to track the changes in the course repository, you should start by
  ```
  git remote add course_repo https://github.com/ufal/npfl139
  git fetch course_repo
  git checkout --no-track course_repo/master -b BRANCH_NAME
  ```
  which creates a branch `BRANCH_NAME` with the current state of the
  course repository. However, unlike to the previous case, `git pull`
  and `git push` in this branch will not operate on the course repository.
  Therefore, you can then commit to this branch and push it to your own
  repository.

  To update your branch with the changes from the course repository, run
  ```
  git fetch course_repo
  git merge course_repo/master
  ```
  while in your branch. Of course, it might be necessary to resolve conflicts
  if both you and I modified the same lines in the templates.

### TOCEntry: ReCodEx

- _What files can be submitted to ReCodEx?_

  You can submit multiple files of any type to ReCodEx. There is a limit of
  **20** files per submission, with a total size of **20MB**.

- _What file does ReCodEx execute and what arguments does it use?_

  Exactly one file with `py` suffix must contain a line starting with `def main(`.
  Such a file is imported by ReCodEx and the `main` method is executed
  (during the import, `__name__ == "__recodex__"`).

  The file must also export an argument parser called `parser`. ReCodEx uses its
  arguments and default values, but it overwrites some of the arguments
  depending on the test being executed – the template should always indicate which
  arguments are set by ReCodEx and which are left intact.

- _What are the time and memory limits?_

  The memory limit during evaluation is **1.5GB**. The time limit varies, but it should
  be at least 10 seconds and at least twice the running time of my solution.

- _Do agents need to be trained directly in ReCodEx?_

  No, you can pre-train your agent locally (unless specified otherwise in the task
  description).
