class EmailTemplate:
    def __init__(self, subject: str, html_body: str):
        self.subject = subject
        self.html_body = html_body

    def render(self, **kwargs):
        return {
            "subject": self.subject.format(**kwargs),
            "body": self.html_body.format(**kwargs),
        }


class TemplateFactory:
    _templates = {}

    @classmethod
    def get_template(cls, template_name: str):
        if template_name not in cls._templates:
            if template_name == "welcome":
                cls._templates[template_name] = EmailTemplate(
                    subject="Welcome, User!",
                    html_body="<h1>Hello User,</h1><p>Thanks for joining us!</p>",
                )
            elif template_name == "reset":
                cls._templates[template_name] = EmailTemplate(
                    subject="Reset Your Password",
                    html_body="<p>Hi User,</p><p>Click <a href='/'>here</a> to reset your password.</p>",
                )
            else:
                raise ValueError("Unknown template")
        return cls._templates[template_name]


class EmailSender:
    def send_email(self, template_name: str, to_email: str, **data):
        template = TemplateFactory.get_template(template_name)
        rendered = template.render(**data)
        print(f"Sending email to {to_email}")
        print(f"Subject: {rendered['subject']}")
        print(f"Body:\n{rendered['body']}")


email_sender = EmailSender()
email_sender.send_email("welcome", "mail@mail.com")
email_sender.send_email("reset", "mail@mail.com")
