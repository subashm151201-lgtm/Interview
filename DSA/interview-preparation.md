# SDU Interview Preparation

This guide explains the Server Diagnostic Utility (SDU) in simple terms and gives you short answers to practice for interviews. The central idea is: SDU discovers server hardware, finds the diagnostic tests that fit it, accepts requests through a Redfish API, and reports test progress and results.

## Q1. Explain the SDU architecture

Think of SDU as a server check-up service. It has four main parts:

1. **Hardware inventory** collects details about the server and components such as CPUs, memory, storage, and network adapters. It saves the information in a JSON cache.
2. **Test discovery** compares the hardware inventory with the test catalog and creates a list of tests that apply to this server.
3. **Redfish API** lets a client browse available tests, select components, and request diagnostics.
4. **Test execution** runs the selected diagnostic commands and records their status and results.

**Interview answer:**

> “SDU has four main parts: hardware inventory, catalog-based test discovery, a Redfish REST interface, and test execution. It discovers the server’s components, determines which catalog tests apply, exposes those tests through Redfish, then runs the tests requested by the client and reports their status.”

## Q2. Why did you use Python?

Python coordinates the different parts of SDU. It is useful for reading and writing JSON, applying rules to hardware data, providing REST API handlers, validating test parameters, and starting and tracking diagnostic commands. Some diagnostics themselves run through shell scripts or bundled tools; Python connects those tools to the inventory, catalog, API, and status reporting.

**Interview answer:**

> “I used Python because SDU needs to coordinate several kinds of work: process hardware and catalog data, provide REST APIs, validate requests, and launch diagnostic tools. Python makes that control logic easier to organize, while the diagnostic work can be done by the appropriate scripts or tools.”

## Q3. How does your application identify the server hardware?

The inventory component gathers server and component details using server properties and component discovery plugins. The project uses sources and tools such as `lshw` and hardware configuration data. It stores the results in a JSON inventory cache, including component details and Redfish resource IDs. SDU uses this inventory to associate tests with the right hardware.

**Interview answer:**

> “SDU uses an inventory layer to collect details about the server and its components. It stores those details in a JSON cache, including component identifiers and Redfish resource IDs. The test discovery logic then uses that inventory to understand what hardware is present.”

## Q4. How do you decide which diagnostic test to execute?

There are two decisions:

1. **Which tests apply to the server?** The catalog defines tests, their categories, their supported modes, and the commands to run. Discovery compares those definitions with the hardware inventory. For example, a test may only apply when a supported GPU or storage controller is present.
2. **Which test runs now?** A client sends a Redfish request naming the test type and target. It can also provide parameters. SDU validates the request and runs the matching test.

In short, the catalog defines tests, hardware discovery filters the list, and the client request chooses what runs now.

**Interview answer:**

> “The catalog defines the available tests and their commands. During discovery, SDU checks the catalog against the hardware inventory and only exposes applicable tests. When a client sends a Redfish request, it selects a test type and target; SDU then runs that test with the requested parameters and tracks the result.”

## Q5. What is the Redfish API?

Redfish is a standard way for software to inspect and manage servers over HTTP. It represents server information as resources with URLs and usually sends data as JSON. SDU exposes diagnostic information and actions under Redfish paths.

**Interview answer:**

> “Redfish is a standard HTTP API for server management. A client can read server resources or request actions using URLs, HTTP methods, and JSON.”

## Q6. Why Redfish instead of IPMI?

Redfish and IPMI have different roles. IPMI is a lower-level management interface. Redfish provides a web API with structured resources and JSON, which makes it convenient for management software to discover components, address them by URI, and request actions. They can coexist; choosing Redfish for SDU’s client-facing API does not mean IPMI is absent from the wider system.

**Interview answer:**

> “Redfish gives SDU a structured, resource-based HTTP interface that management clients can use to discover hardware and request diagnostics. IPMI is a different, lower-level management interface, and the two can coexist.”

## Q7. How do you launch a diagnostic task through Redfish?

The client sends a **POST** request to SDU’s diagnostic Start action with JSON describing the targets and test type, such as `Quick`. SDU validates the request, creates a task ID, starts diagnostics in a background thread, and responds with **202 Accepted** and task information.

**Interview answer:**

> “The client POSTs a JSON request with the target components and test type to the Redfish Start action. SDU validates it, creates a task, starts the work asynchronously, and returns 202 with the task information.”

## Q8. How do you monitor an asynchronous task?

Diagnostics can take time, so the start request returns a task reference instead of waiting for all tests to finish. The client sends **GET** requests to the task resource, `/redfish/v1/TaskService/Tasks/<task_id>`, to check its state and progress.

**Interview answer:**

> “Because diagnostics can take time, the start request returns a task reference instead of waiting for everything to finish. The client polls the task resource with GET to see whether it is running, completed, failed, or cancelled, and to check progress.”

## Q9. How do you cancel a task?

SDU provides a **Cancel action**. The client sends a POST request with the targets to cancel. The API validates the targets and asks the diagnostic core to cancel the selected running or queued tests. The task status is updated to reflect cancellation.

**Interview answer:**

> “The client POSTs to the Redfish Cancel action with the target components. SDU validates the request and cancels the selected running or queued tests. The task status then reflects the cancellation.”

## Q10. How do you handle API failures?

SDU validates requests before acting. It checks identifiers, JSON content, targets, and diagnostic options. It returns Redfish-formatted errors with suitable HTTP status codes. For example, invalid requests can return **400**, a conflicting task can return **409**, and an internal failure can return **500**. Asynchronous task failures are also recorded in the task status.

**Interview answer:**

> “I validate the request before starting work and return Redfish-formatted errors with suitable HTTP status codes. For asynchronous work, I also update the task state so the client can see if it failed.”

## Q11. What authentication does the API use?

The SDU Flask route handlers validate requests and targets, but the reviewed handlers do not implement authentication themselves. Authentication needs to be provided by the surrounding service or deployment. Verify the actual deployed Redfish front end before naming a scheme such as Basic authentication or session tokens.

**Interview answer:**

> “The SDU route code I reviewed does not implement authentication directly. Authentication would need to be provided by the surrounding service or deployment. I would verify the deployed Redfish front end before claiming a specific authentication scheme.”

## Q12. What is REST?

REST is an API design style based on resources. Each resource has a URL, and clients use standard HTTP methods to read or change it. SDU exposes resources and actions for diagnostics and tasks.

**Interview answer:**

> “REST is an API design style where resources are identified by URLs and manipulated using HTTP methods, usually with JSON data.”

## Q13. What is the difference between REST and SOAP?

REST is an API design style that uses web concepts such as URLs, HTTP methods, and often JSON. SOAP is a messaging protocol with a defined XML message format and formal conventions for describing services and messages. SDU’s API follows the REST style and uses JSON.

**Interview answer:**

> “REST commonly uses HTTP methods and JSON resources. SOAP uses structured XML messages and a more formal messaging protocol. SDU’s API follows the REST style and uses JSON.”

## Q14. What are GET, POST, PUT, PATCH, and DELETE?

- **GET** reads a resource. For example, check a task’s status.
- **POST** submits data or requests an action. For example, start diagnostics.
- **PUT** replaces a resource with a complete new version.
- **PATCH** changes selected fields of a resource.
- **DELETE** removes a resource or requests its deletion.

In SDU, both starting and cancelling diagnostics use POST action endpoints. Diagnostic cancellation is not the same as deleting a task resource.

**Interview answer:**

> “GET reads data, POST submits data or triggers an action, PUT replaces a resource, PATCH updates part of a resource, and DELETE removes a resource. In SDU, diagnostic start and cancel are POST actions.”

## Q15. What is idempotency?

An operation is **idempotent** if repeating the same request has the same intended effect as sending it once. GET is normally safe to repeat because reading task status does not change the task. Starting diagnostics is an action, so repeating it could start work again. SDU checks for a task already in progress and can return **409 Conflict** rather than starting another one.

**Interview answer:**

> “Idempotency means repeating a request does not keep changing the result. GET is normally safe to repeat. Starting diagnostics is an action, so I would not assume it is safe to repeat; SDU checks for an already-running task and can return 409.”

## Quick glossary

- **Catalog:** The list of test definitions and commands.
- **Hardware inventory:** The discovered components in the server.
- **Redfish resource ID:** An API address that identifies a server or component.
- **Quick / Comprehensive:** Diagnostic modes; a test can support either or both.
- **Asynchronous task:** Work that continues after the API has returned a response. The client checks its task resource for progress and results.
