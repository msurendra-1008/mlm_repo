{% if firm.tender_status == "Pending"%}
                            {% comment %} <a href="" class="btn btn-primary">View</a>
                            <a href="" class="btn btn-success mt-2">Edit</a> {% endcomment %}
                            
                            <form method="GET" action="{% url 'tender_accept'%}">
                                {% csrf_token %}
                                <input type="hidden" name="pk" value="{{firm.pk}}">
                            <button type="submit" class="btn btn-warning mt-2" >
                                 Accept
                            </button>
                            </form>
                            <form method="GET" action="{% url 'tender_reject'%}">
                                {% csrf_token %}
                                <input type="hidden" name="pk" value="{{firm.pk}}">
                            <button type="submit" class="btn btn-danger mt-2" >
                                 Reject
                            </button>
                            </form>
                           
                            {% endif %}

{% if firm.tender_status == "Pending" %}
                            <i class="fa fa-square-o" aria-hidden="true" style="color: red"> {{firm.tender_status}}</i>
                            {% elif firm.tender_status == "Accepted" %}
                            <i class="fa fa-check-square-o" aria-hidden="true" style="color: green;"> {{firm.tender_status}}</i>
                            {% else %}
                            <i class="fa fa-times" aria-hidden="true" style="color: red;"> {{firm.tender_status}}</i>
                            {% endif %}


### changes in node file.


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/project/mlm_repo
ExecStart=/home/ubuntu/project/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/project/mlm_repo.sock mlm.wsgi:application

[Install]
WantedBy=multi-user.target

server {
    listen 80;
    server_name 3.110.90.176;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/project/mlm_repo.sock;
    }
}

sudo systemctl daemon-restart
sudo systemctl restart junicorn
sudo systemctl restart nginx