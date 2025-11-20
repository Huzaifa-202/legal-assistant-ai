from app import create_app

# Gunicorn with aiohttp will call this async function
# Do NOT use asyncio.run() here
app = create_app



Logs


Instances
Lookback period
Connected!
2025-11-20T16:27:42.2166913Z    _____
2025-11-20T16:27:42.2167211Z   /  _  \ __________ _________   ____
2025-11-20T16:27:42.2167326Z  /  /_\  \\___   /  |  \_  __ \_/ __ \
2025-11-20T16:27:42.2167348Z /    |    \/    /|  |  /|  | \/\  ___/
2025-11-20T16:27:42.2167368Z \____|__  /_____ \____/ |__|    \___  >
2025-11-20T16:27:42.2167533Z         \/      \/                  \/
2025-11-20T16:27:42.216756Z A P P   S E R V I C E   O N   L I N U X
2025-11-20T16:27:42.2167578Z
2025-11-20T16:27:42.21676Z Documentation    : http://aka.ms/webapp-linux
2025-11-20T16:27:42.2167621Z Python quickstart: https://aka.ms/python-qs
2025-11-20T16:27:42.2167642Z Python version   : 3.12.12
2025-11-20T16:27:42.2167662Z Instance Name    : lw1sdlwk000853
2025-11-20T16:27:42.216769Z Instance Id      : 91baf352954053b10aec40a76c08c5d8df4b45053890ea68ab5fc855af1343fa
2025-11-20T16:27:42.2167709Z
2025-11-20T16:27:42.2167755Z Note: Any data outside '/home' is not persisted
2025-11-20T16:27:45.8061153Z Starting OpenBSD Secure Shell server: sshd.
2025-11-20T16:27:45.8365996Z WEBSITES_INCLUDE_CLOUD_CERTS is not set to true.
2025-11-20T16:27:45.9450476Z Updating certificates in /etc/ssl/certs...
2025-11-20T16:28:32.89603Z rehash: warning: skipping duplicate certificate in azl_Sectigo_Public_Server_Authentication_Root_R46.pem
2025-11-20T16:28:32.9159699Z rehash: warning: skipping duplicate certificate in azl_Sectigo_Public_Server_Authentication_Root_E46.pem
2025-11-20T16:28:32.9168148Z rehash: warning: skipping duplicate certificate in azl_SSL.com_TLS_RSA_Root_CA_2022.pem
2025-11-20T16:28:32.9374853Z rehash: warning: skipping duplicate certificate in azl_SSL.com_TLS_ECC_Root_CA_2022.pem
2025-11-20T16:28:33.041492Z 4 added, 0 removed; done.
2025-11-20T16:28:33.0419024Z Running hooks in /etc/ca-certificates/update.d...
2025-11-20T16:28:33.0530568Z done.
2025-11-20T16:28:33.0929292Z CA certificates copied and updated successfully.
2025-11-20T16:28:33.2566288Z Site's appCommandLine: gunicorn main:app --worker-class aiohttp.GunicornWebWorker -w 1 -b 0.0.0.0:$PORT
2025-11-20T16:28:33.2566715Z
2025-11-20T16:28:33.2566751Z
2025-11-20T16:28:33.2566769Z
2025-11-20T16:28:33.2566786Z
2025-11-20T16:28:33.2566802Z
2025-11-20T16:28:33.2566817Z
2025-11-20T16:28:33.2566922Z
2025-11-20T16:28:33.8124933Z Starting periodic command scheduler: cron.
2025-11-20T16:28:33.8400978Z Launching oryx with: create-script -appPath /home/site/wwwroot -output /opt/startup/startup.sh -virtualEnvName antenv -defaultApp /opt/defaultsite -userStartupCommand 'gunicorn main:app --worker-class aiohttp.GunicornWebWorker -w 1 -b 0.0.0.0:$PORT
2025-11-20T16:28:33.8401662Z
2025-11-20T16:28:33.8401699Z
2025-11-20T16:28:33.8401718Z
2025-11-20T16:28:33.8401733Z
2025-11-20T16:28:33.8401747Z
2025-11-20T16:28:33.8401762Z
2025-11-20T16:28:33.8409452Z '
2025-11-20T16:28:34.2335262Z Could not find build manifest file at '/home/site/wwwroot/oryx-manifest.toml'
2025-11-20T16:28:34.2347952Z Could not find operation ID in manifest. Generating an operation id...
2025-11-20T16:28:34.2624722Z Build Operation ID: bef0c9ed-4bd5-40f4-9d5b-5db5e416eda3
2025-11-20T16:28:35.2673719Z Oryx Version: 0.2.20251017.2, Commit: 482d4c55e818733ab33b9d2131f9dc485a21fd03, ReleaseTagName: 20251017.2
2025-11-20T16:28:35.3561496Z Writing output script to '/opt/startup/startup.sh'
2025-11-20T16:28:35.5000127Z WARNING: Could not find virtual environment directory /home/site/wwwroot/antenv.
2025-11-20T16:28:35.5011406Z WARNING: Could not find package directory /home/site/wwwroot/__oryx_packages__.
2025-11-20T16:28:38.3943794Z
2025-11-20T16:28:38.4207978Z Error: class uri 'aiohttp.GunicornWebWorker' invalid or not found:
2025-11-20T16:28:38.4208068Z
2025-11-20T16:28:38.42081Z [Traceback (most recent call last):
2025-11-20T16:28:38.4208126Z   File "/opt/python/3.12.12/lib/python3.12/site-packages/gunicorn/util.py", line 110, in load_class
2025-11-20T16:28:38.4208206Z     mod = importlib.import_module('.'.join(components))
2025-11-20T16:28:38.4208229Z           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-11-20T16:28:38.4208253Z   File "/opt/python/3.12.12/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-11-20T16:28:38.4208276Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-11-20T16:28:38.4208298Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-11-20T16:28:38.4208321Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-11-20T16:28:38.4208344Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-11-20T16:28:38.4208368Z   File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
2025-11-20T16:28:38.4208389Z ModuleNotFoundError: No module named 'aiohttp'
2025-11-20T16:28:38.4208408Z ]
2025-11-20T16:28:38.4208932Z
2025-11-20T16:33:37.420Z No new trace in the past 1 min(s).
2025-11-20T16:34:37.420Z No new trace in the past 2 min(s).
