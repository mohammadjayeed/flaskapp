### Docker instructions

```bash 
docker build -t ${any_name} . 
```
```bash 
docker run -dp 5000:5000 ${name_given_in_the_previous_command} 
```

### Enter the Container
```bash
docker exec -it ${container_name/id} /bin/bash
```

### Project Sample
<img src="images/Untitled.png" >