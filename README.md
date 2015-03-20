# kafka-python-bolt
Template project for a Kafka stream processing node.

# Usage
Clone this project into a directory for your app (`your_app`).
```
git clone https://github.com/mfaulk/kafka-python-bolt.git your_app
cd your_app
```
You will deploy your app by referencing a GitHub repository. Create a new GitHub repository (e.g. https://github.com/user/newrepo.git) for your app, and change the origin of this cloned project:

```
git remote rm origin
git remote add origin https://github.com/user/newrepo.git
```

The command `git remote -v` should now show

```
origin  https://github.com/user/newrepo.git (fetch)
# origin  https://github.com/user/newrepo.git (push)
```

Edit `configure.sh` so that APP_NAME is the desired name of your app, and GIT_REPO is the URL of your GitHub repository. Run this script to generate a [Fleet unit file](https://coreos.com/docs/launching-containers/launching/fleet-unit-files/) for your app named <APP_NAME>.service

```
./configure.sh
```

## Writing your app
Define your stream processing node by declaring the input stream topics, output stream topics, and `execute` method in `app/bolt.py`

Commit and push all changes to GitHub

```
git add *.service
git commit -am 'Adds generated Fleet unit file'
git push
```

