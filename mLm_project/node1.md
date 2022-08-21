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