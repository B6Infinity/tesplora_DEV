**NOTE:**

1. All dummy users have the same password: `pass_123`
2. There are 4 classes for an *ALERT MESSAGE:*
    i. `success`
    ii. `error`
    iii. `warning`
    iv. `info`
3. HTML Django Template to execute HTML if user is *PREMIUM* user: 
    `{% if user.profile.is_premium_user %}HTML/JS/CSS TO SHOW HERE{% endif %}`
