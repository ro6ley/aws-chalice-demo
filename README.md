[![HitCount](http://hits.dwyl.io/ro6ley/aws-chalice-demo.svg)](http://hits.dwyl.io/ro6ley/aws-chalice-demo)

# Chalice Demo App for AWS Lambda Deployment

This repository contains the code for this [blogpost]() on [StackAbuse](https://stackabuse.com/).

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [VirtualEnv](https://virtualenv.pypa.io/en/latest/installation/)
- [ ] [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [ ] AWS Account and credentials: `secret key` and `access ID`
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/ro6ley/aws-chalice-demo.git
```

2. Check into the cloned repository
```
$ cd aws-chalice-demo
```

3. Set up the virtualenvironment:
```
$ virtualenv --python=python3 venv
```

4. Install the requirements
```
$ pip install -r demoapp/requirements.txt
```

4. Deploy the application on AWS Lambda:
```
$ chalice deploy
```

5. Interact with the API on the URL returned by the command above.

## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
