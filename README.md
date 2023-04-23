<h1>Testing BitBucket piplines with deploying in k8s cluster within Yandex Cloud. </h1>

1) Before you need to create service account in yandex cloud
with roles editor and container-registry.images.puller.
2) If you don't have already signed in your yandex cloud account (not in service!) do that follow instruction:
   https://cloud.yandex.ru/docs/cli/operations/profile/profile-create#interactive-create
3) Create authorization key for service account
```
yc iam key create --service-account-name <service_account_name> --output key.json --folder-id <catalog_ID>
```
4) Create next secrets in your repo:
<ul>
    <li><b>YC_AUTH_KEY_JSON</b> - content of key.json, generated in step 3</li>
    <li><b>CLOUD_ID</b> - check step 5</li>
    <li><b>FOLDER_ID</b> - check step 6</li>
    <li><b>K8S_ID</b> - check step 7</li>
    <li><b>REGISTRY_ID</b> - check step 8</li>
    <li><b>APPLICATION_ENV_DATA</b> - content of .env file. You have to create custom one with own variables based on ./prod/.env.example</li>
    <li><b>APP_IP</b> - IP address you application will be running. For more details check step 9</li>
</ul>

5) How to get cloud id
```
yc resource-manager cloud list  # choose one that you need
```

6) How to get folder id
```
yc resource-manager folder list  # choose one that you need
```

7) How to get kubernetes cluster id
```
yc managed-kubernetes cluster list  # choose one that you need
```

8) How to get docker registry id
``` 
yc container registry list  # choose one that you need
```

9) If you do not have own static IP yet, you can create it in 
Virtual Private Cloud -> IP addresses -> Reserve an address.
If you don't select IP, kubernetes will give to your service random IP.
