var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'vitinho030605@gmail.com',
    pass: 'vt485276'
  }
});

var mailOptions = {
  from: 'vitinho030605@gmail.com',
  to: 'vitorcdn11@gmail.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
