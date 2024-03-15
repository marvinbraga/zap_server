# Zap Server

**Python TCP server to interact with WhatsApp, etc.**

[![Zap Server Actions](https://github.com/marvinbraga/zap_server/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/marvinbraga/zap_server/actions/workflows/pythonapp.yml)
[![Updates](https://pyup.io/repos/github/marvinbraga/zap_server/shield.svg)](https://pyup.io/repos/github/marvinbraga/zap_server/)
[![Python 3](https://pyup.io/repos/github/marvinbraga/zap_server/python-3-shield.svg)](https://pyup.io/repos/github/marvinbraga/zap_server/)

## Available Commands

## Command List:

**People:**

* No commands available at the moment.

**Groups:**

* Create group (GroupCreate)
* Get invite link (GroupGetInviteLink)
* Rename group (GroupRename)
* Set group picture (GroupSetPicture)
* Allow only administrators to send messages (GroupOnlyAdminsSendMessages)
* Allow all members to send messages (GroupAllUsersSendMessages)
* Allow only administrators to change group data (GroupOnlyAdminsChangeGroupData)
* Allow all members to change group data (GroupAllUsersChangeGroupData)
* Get number of group participants (GroupParticipantCount)
* List group participants (GroupParticipants)
* Join a group (GroupJoin)
* Leave a group (GroupExit)

**Management:**

* Exit the application (Quit)

**Messages:**

* Send message (SendMessage)
* Send picture (SendPicture)
* Send document (SendDocument)

**Properties:**

* Get QR code (GetQrCode)
* Check point (CheckPoint)
* Check if connected (IsConnected)

## Env File

**Creating the .env File**

To configure the server's environment variables, you need to create a `.env` file in the project's root directory. This
file can be created from the `contrib/env-sample` file:

```bash
cp contrib/env-sample .env
```

**Adjusting Environment Variables**

The `.env` file contains several environment variables that can be customized according to your needs. Here's how your
provided variables would fit in:

```
AUTH_KEY=7de5b6a7-072b-4476-aed5-7bb54b423bb4  # Authentication key
SITE_ROOT=yourdomain.com                        # Base URL for your website
EMAIL_HOST=imap.yourhost.com                    # IMAP email server
EMAIL_HOST_USER=your_email@yourdomain.com       # Your email address
EMAIL_PASSWORD=mail_pass                        # Your email password
EMAIL_PORT=587                                  # IMAP email port (standard)
URL_MEDIA_GROUPS=http://localhost:5000/media/images/groups   # URL for accessing group images
TEST_CONTACT_GROUP_MEMBER="Your Name"           # Test contact name (might be application-specific)
```

**Important Notes:**

* **Replace placeholders:** Change `yourdomain.com`, `your_email@yourdomain.com`, and `mail_pass` to their actual
  values.
* **Security:** Protect your `.env` file. It shouldn't be committed to version control.

## How to Start the Server

```bash
python main.py 0.0.0.0 8777
```

## How to Test

```python
# apps/client_app.py

from multiprocessing.connection import Client
from threading import Thread

from core import settings


def connect_to_server():
    """
    Method to connect to server.
    """
    c = Client(('127.0.0.1', 8777), authkey=settings.AUTH_KEY.encode())
    commands = [
        'user_token||SendMessage||Group Name||Message Test by Client.',
        # 'user_token||GroupGetInviteLink||Group Name',
        # 'user_token||GroupOnlyAdminsChangeGroupData||Group Name',
        # 'user_token||GroupAllUsersChangeGroupData||Group Name',
        # 'user_token||GroupOnlyAdminsSendMessages||Group Name',
        # 'user_token||GroupAllUsersSendMessages||Group Name',
        # 'user_token||GroupOnlyAdminsSendMessages||Group Name',
        # 'user_token||IsConnected',
    ]
    try:
        for command in commands:
            c.send(command)
            resp = c.recv()
            print(f'Response: {resp}')
    except ConnectionRefusedError:
        print('Operation Canceled: Server refused connection.')
    except ConnectionError as e:
        print(f'Operation canceled: {str(e)}.')


if __name__ == '__main__':
    t = Thread(target=connect_to_server)
    t.start()
    t.join()
```

## Modifying WhatsApp Elements

The `server/adapters/the_first/elements/data.py` file contains a dictionary that maps WhatsApp elements to their respective XPath paths or CSS selectors.
These elements are used to interact with the WhatsApp interface through an automation tool like Selenium.

If there are changes to the HTML structure of WhatsApp that affect the element paths, you'll need to update the
dictionary in the `data.py` file to reflect those changes. Here are the steps to modify the elements:

1. **Identify the element:** Determine which WhatsApp element needs to be updated. The elements are mapped to specific
   keys in the dictionary, such as `search_edit`, `qr_code`, `send_message`, etc.

2. **Inspect the element:** Using the browser's developer tools, inspect the corresponding element on the WhatsApp page.
   Locate the updated XPath path or CSS selector for that element.

3. **Update the dictionary:** In the `data.py` file, find the key corresponding to the element you want to update.
   Replace the value associated with that key with the new XPath path or CSS selector you obtained in the previous step.

4. **Test the changes:** After updating the dictionary, run the code that uses those elements to ensure that the changes
   work correctly. Verify that the interaction with WhatsApp occurs as expected.

5. **Save and commit the changes:** Once you have tested and verified that the changes are working, save the `data.py`
   file and commit the changes to the repository.

Keep in mind that any changes to the WhatsApp elements may affect the functionality of the code that interacts with
those elements. Therefore, it's important to exercise caution when making changes and thoroughly test them before
deploying to a production environment.

If you have any questions or need assistance with updating the WhatsApp elements, feel free to open an issue in the
project repository.

## Contributing to the GitHub Project

**Welcome!** We appreciate your interest in contributing to our project on GitHub. Your participation is essential for
the evolution and improvement of the code.

**Here are some ways to contribute:**

* **Reporting Bugs:**
    * Find the project repository on GitHub.
    * Click on "Issues" and then on "New Issue".
    * Describe the bug clearly and concisely, including details such as the software version, operating system, and
      steps to reproduce it.

* **Suggesting Improvements:**
    * Follow the same steps as for reporting bugs, but select "New Feature" instead of "New Issue".
    * Describe the improvement you would like to see, including its benefits and impact on the project.

* **Submitting Pull Requests:**
    * Fork the repository to your GitHub profile.
    * Create a new branch for your modification.
    * Implement your change and test it.
    * Submit a pull request to the original repository, with a clear description of your changes.

* **Participating in Discussions:**
    * Access the "Issues" section and read the open discussions.
    * Comment on issues that you have knowledge of or are interested in contributing to.
    * Answer questions from other collaborators and share your knowledge.

**Tips for Contributing:**

* **Read the project documentation:** Familiarize yourself with the code and the contribution guidelines.
* **Start with small contributions:** Start with simple bugs or minor improvements.
* **Communicate clearly:** Be clear and concise when reporting bugs, suggesting improvements, or submitting pull
  requests.
* **Be patient:** Pull requests can take time to be reviewed and merged.

**By contributing to this project, you are helping to build a vibrant and collaborative community.** We appreciate your
participation!

**Thank you for contributing!**