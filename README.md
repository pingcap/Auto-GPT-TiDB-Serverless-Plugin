# Auto-GPT-TiDB-Serverless-Plugin
> Still under developement

## Commands
- `tidb_sql_executor`, directly exectue sql in your tidb database

## Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository, or download the repository as a zip file.
  
   ![Download Zip](https://raw.githubusercontent.com/BillSchumacher/Auto-GPT/master/plugin.png)

2. **Install the plugin's dependencies:**
   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   If you cloned the repository, compress the plugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPTTiDB
   ```

   If the plugin is not allowlisted, you will be warned before it's loaded.

## Configure Enviroments

Add following code in `Auth-GPT/.env`

```shell
TIDB_HOST="gateway01.<your-region>.prod.aws.tidbcloud.com"
TIDB_PORT=4000
TIDB_USER="<your-user>"
TIDB_PASSWORD="<your-password>"
TIDB_DATABASE="<your-database>"
```

## Example

https://user-images.githubusercontent.com/10102304/234223704-1ca4d2da-9848-44fb-9498-6be50f39a574.mp4
