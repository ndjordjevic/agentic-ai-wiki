# x74353/Amphetamine

## Metadata
- Stars: 119
- Primary language: AppleScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: (none)
- Fetched: 2026-08-20
- Final URL: https://github.com/x74353/Amphetamine

## Description
Additional Amphetamine Resources

## README
# Hello 👋🏼

On Apple Silicon Mac laptops, Closed-Display Mode may not work as expected after connecting or disconnecting your Mac from an external power source such as a power adapter or display with power delivery. To avoid any issues, you can install a script and configuration file that addresses the issue.

I'm truly sorry for this, but Apple provides no other way. Apple thinks they know better than you do, and won't allow you to permit Amphetamine to directly install the script and configuration file needed to avoid issues with Closed-Display Mode. To get things to "just work" nowadays, you have to do it yourself it seems. 🔨💪🏼

---

# How To Install Power Protect

1. **[Download the Power Protect script](https://raw.githubusercontent.com/x74353/Amphetamine/master/Files/PowerProtect_Script.zip)** and install it in the following location:
    ```/Users/YourUserAccount/Library/Application Scripts/com.if.Amphetamine/```

2. **[Download the Power Protect configuration file](https://raw.githubusercontent.com/x74353/Amphetamine/master/Files/PowerProtect_Configuration.zip)** and install it in the following location:
    ```/private/etc/sudoers.d/```

3. Open Terminal.app from `/Applications/Utilities/`, then copy & paste the following command into a Terminal window:

    ```defaults write com.if.Amphetamine 'Enable Power Protect Install' -bool TRUE```

   then press the Return key to execute the command

## Top-level structure
- `Files/` — zip archives for Power Protect script and configuration file (AppleScript + sudoers entry)
  - `PowerProtect_Configuration.zip` — sudoers.d entry granting passwordless privilege escalation for the power event monitor
  - `PowerProtect_Script.zip` — AppleScript that monitors power source changes and re-asserts Closed-Display Mode
  - `amphetamine_PowerProtect` — compiled script bundle
  - `powerProtect.scpt` — raw AppleScript source
- `Localized/` — localization strings for the Amphetamine macOS app
- `LICENSE.md` — MIT License
- `Power_Protect_English` — English-language instructions file
- `README.md` — installation guide for Power Protect on Apple Silicon
