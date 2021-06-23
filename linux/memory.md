# To Find All the Process ID

- `top` to view memory status of vm machine

# To Find details of the running services

- Show all process: `ps -e | grep processname` 
- Show with full format: `ps -f | grep processname`
- Show all together: `ps -ef | grep processname`
- Example:
    ```
    ps -ef | grep java
    ```
