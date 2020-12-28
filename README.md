# VkOnline
Скрипт на вечный онлайн vk. Cron должен запускать его каждую минуту.

# requirements
 * [vk_api](https://pypi.org/project/vk-api/)
 
# usage
```python
token = '<access_token>'  #  <-- вставьте сюда свой токен
```
 Токен можно взять [здесь](https://oauth.vk.com/authorize?client_id=6121396&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1)
 
 
## cron example
 ```
 * * * * * python3 /home/tomasgl/VkOnline/api.py  # запускать скрипт каждую минуту
```
