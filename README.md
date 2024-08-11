# env_sourcer

Do you hate .env files? Then, the env_sourcer is for you.

There are only a few rules for the env_sourcer. Primarily, you'll need a folder called 'envs'
That's pretty much it. Other than this, you'll need your env file that will end in some version of '.local', '.prod', or '.stg' there are other versions you can specify. You can call these files whatever you want. The only other requirement is that you run `export ENVIRONMENT=<your_specified_environment>` in CLI.

After you fill in your env file, import the env_sourcer by running:
`from env_sourcer.services.env_sourcer import EnvSourcer`
in your python script

Create your env_sourcer: `env_sourcer = EnvSourcer()`

Access env variables: `env_sourcer.api_key`

Look at the tests if you would like to see other examples of using the env_sourcer
