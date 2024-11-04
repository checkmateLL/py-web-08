Task 1

Cloud MongoDB

![image](https://github.com/user-attachments/assets/b98a4e24-803c-46e5-98ef-0a50fa8ef3b6)

Authors cocntent

![image](https://github.com/user-attachments/assets/4453649b-2f47-4dfe-a02b-0e0673ec3302)

Quotes content

![image](https://github.com/user-attachments/assets/c0e1d9fd-35dc-4c2f-a7ac-fd1cb838099c)



Task 2

Docker
![image](https://github.com/user-attachments/assets/bce21ba0-cab2-417b-a8fd-5b3e2fb60b9b)

Log of prosucer.py:
```
E:\Education\GoIT\Python\py-web-08\part-two>python prosucer.py
2024-11-04 14:25:06,429 - INFO - Successfully connected to MongoDB
2024-11-04 14:25:06,432 - INFO - Pika version 1.3.2 connecting to ('::1', 5672, 0, 0)
2024-11-04 14:25:06,433 - INFO - Socket connected: <socket.socket fd=980, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63938, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:25:06,434 - INFO - Streaming transport linked up: (<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30>, _StreamingProtocolShim: <SelectConnection PROTOCOL transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>).
2024-11-04 14:25:06,488 - INFO - AMQPConnector - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:25:06,488 - INFO - AMQPConnectionWorkflow - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:25:06,488 - INFO - Connection workflow succeeded: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:25:06,488 - INFO - Created channel=1
2024-11-04 14:25:06,492 - INFO - Successfully connected to RabbitMQ
2024-11-04 14:25:07,117 - INFO - Contact 1/10: Cynthia Silva added to sms_queue
2024-11-04 14:25:07,177 - INFO - Contact 2/10: David Richardson added to email_queue
2024-11-04 14:25:07,237 - INFO - Contact 3/10: Dr. Kenneth Griffin Jr. added to email_queue
2024-11-04 14:25:07,313 - INFO - Contact 4/10: Gregory Moore added to sms_queue
2024-11-04 14:25:07,374 - INFO - Contact 5/10: Jessica Carr added to email_queue
2024-11-04 14:25:07,434 - INFO - Contact 6/10: Cynthia Bartlett added to email_queue
2024-11-04 14:25:07,494 - INFO - Contact 7/10: Allison Moody added to email_queue
2024-11-04 14:25:07,555 - INFO - Contact 8/10: Matthew Ruiz added to email_queue
2024-11-04 14:25:07,613 - INFO - Contact 9/10: Kristopher Hayes added to sms_queue
2024-11-04 14:25:07,674 - INFO - Contact 10/10: Lindsay Luna added to email_queue
2024-11-04 14:25:07,674 - INFO - Successfully generated all contacts
2024-11-04 14:25:07,675 - INFO - Closing connection (200): Normal shutdown
2024-11-04 14:25:07,675 - INFO - Closing channel (200): 'Normal shutdown' on <Channel number=1 OPEN conn=<SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>
2024-11-04 14:25:07,676 - INFO - Received <Channel.CloseOk> on <Channel number=1 CLOSING conn=<SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000027031D0BD30> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>
2024-11-04 14:25:07,676 - INFO - Closing connection (200): 'Normal shutdown'
2024-11-04 14:25:07,678 - INFO - Aborting transport connection: state=1; <socket.socket fd=980, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63938, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:25:07,678 - INFO - _AsyncTransportBase._initate_abort(): Initiating abrupt asynchronous transport shutdown: state=1; error=None; <socket.socket fd=980, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63938, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:25:07,678 - INFO - Deactivating transport: state=1; <socket.socket fd=980, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63938, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:25:07,678 - INFO - AMQP stack terminated, failed to connect, or aborted: opened=True, error-arg=None; pending-error=ConnectionClosedByClient: (200) 'Normal shutdown'
2024-11-04 14:25:07,678 - INFO - Stack terminated due to ConnectionClosedByClient: (200) 'Normal shutdown'
2024-11-04 14:25:07,679 - INFO - Closing transport socket and unlinking: state=3; <socket.socket fd=980, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63938, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:25:07,679 - INFO - User-initiated close: result=BlockingConnection__OnClosedArgs(connection=<SelectConnection CLOSED transport=None params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>, error=ConnectionClosedByClient: (200) 'Normal shutdown')
```

Log of consumer-mail.py
```
E:\Education\GoIT\Python\py-web-08\part-two>python consumer-mail.py
2024-11-04 14:24:02,506 - INFO - Successfully connected to MongoDB
2024-11-04 14:24:02,508 - INFO - Pika version 1.3.2 connecting to ('::1', 5672, 0, 0)
2024-11-04 14:24:02,509 - INFO - Socket connected: <socket.socket fd=948, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63899, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:24:02,510 - INFO - Streaming transport linked up: (<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x00000194DBF48A60>, _StreamingProtocolShim: <SelectConnection PROTOCOL transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x00000194DBF48A60> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>).
2024-11-04 14:24:02,561 - INFO - AMQPConnector - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x00000194DBF48A60> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:24:02,562 - INFO - AMQPConnectionWorkflow - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x00000194DBF48A60> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:24:02,562 - INFO - Connection workflow succeeded: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x00000194DBF48A60> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:24:02,562 - INFO - Created channel=1
2024-11-04 14:24:02,569 - INFO - Started consuming email queue. To exit press CTRL+C
2024-11-04 14:25:07,550 - INFO - Simulating email sending to David Richardson at joyce22@example.com
2024-11-04 14:25:08,623 - INFO - Email sent and status updated for David Richardson
2024-11-04 14:25:08,679 - INFO - Simulating email sending to Dr. Kenneth Griffin Jr. at jeffrey35@example.org
2024-11-04 14:25:09,743 - INFO - Email sent and status updated for Dr. Kenneth Griffin Jr.
2024-11-04 14:25:09,799 - INFO - Simulating email sending to Jessica Carr at tylerthomas@example.com
2024-11-04 14:25:10,869 - INFO - Email sent and status updated for Jessica Carr
2024-11-04 14:25:10,928 - INFO - Simulating email sending to Cynthia Bartlett at dmaldonado@example.net
2024-11-04 14:25:11,996 - INFO - Email sent and status updated for Cynthia Bartlett
2024-11-04 14:25:12,052 - INFO - Simulating email sending to Allison Moody at thomascase@example.org
2024-11-04 14:25:13,114 - INFO - Email sent and status updated for Allison Moody
2024-11-04 14:25:13,170 - INFO - Simulating email sending to Matthew Ruiz at gregorymcconnell@example.net
2024-11-04 14:25:14,237 - INFO - Email sent and status updated for Matthew Ruiz
2024-11-04 14:25:14,292 - INFO - Simulating email sending to Lindsay Luna at heather51@example.net
2024-11-04 14:25:15,353 - INFO - Email sent and status updated for Lindsay Luna
```

Log of consumer-sms.py
```
E:\Education\GoIT\Python\py-web-08\part-two>python consumer-sms.py
2024-11-04 14:24:33,983 - INFO - Successfully connected to MongoDB
2024-11-04 14:24:33,986 - INFO - Pika version 1.3.2 connecting to ('::1', 5672, 0, 0)
2024-11-04 14:24:33,987 - INFO - Socket connected: <socket.socket fd=1016, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=6, laddr=('::1', 63920, 0, 0), raddr=('::1', 5672, 0, 0)>
2024-11-04 14:24:33,988 - INFO - Streaming transport linked up: (<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000021C2BF88940>, _StreamingProtocolShim: <SelectConnection PROTOCOL transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000021C2BF88940> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>).
2024-11-04 14:24:34,039 - INFO - AMQPConnector - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000021C2BF88940> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:24:34,040 - INFO - AMQPConnectionWorkflow - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000021C2BF88940> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:24:34,040 - INFO - Connection workflow succeeded: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000021C2BF88940> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>
2024-11-04 14:24:34,040 - INFO - Created channel=1
2024-11-04 14:24:34,047 - INFO - Started consuming SMS queue. To exit press CTRL+C
2024-11-04 14:25:07,538 - INFO - Simulating SMS sending to Cynthia Silva at 497.565.6371x95866
2024-11-04 14:25:08,608 - INFO - SMS sent and status updated for Cynthia Silva
2024-11-04 14:25:08,665 - INFO - Simulating SMS sending to Gregory Moore at 613.913.9820
2024-11-04 14:25:09,730 - INFO - SMS sent and status updated for Gregory Moore
2024-11-04 14:25:09,787 - INFO - Simulating SMS sending to Kristopher Hayes at 8937081326
2024-11-04 14:25:10,854 - INFO - SMS sent and status updated for Kristopher Hayes
```






