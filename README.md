# Engineering_F.e.R.a

Able to test parts in the lab, and identify parts using A.I. recognition
<br>
<br>

## Table of Contents
* [Project F.e.](#parts-tester)
   * [Problems and Solutions](#problems-and-solutions)
   * [Description](#description)
   * [Images](#images-progress)
   * [Links](#related-links)


<br>
<br>
## Budget
<br>
$100

   * $50 = party upon completion of Project F.e.
   * $50 = party upon completion of Project R.a.
## Iteration
<br>
<br>
The Pseudocode for the Test Box

```mermaid
flowchart TD
    A(((Human Input))) -->B(Check for plugged in devices)
    B --> C{Device Outputs}
    E[Servos]
    D[Toggle 0-90]
    F[LCD]
    G[Draws text]
    H[Ultrasonic sensor]
    J[LED]
    K[Blinks]
    L[Photocell]
    N[RGB LED] 
    O[OLED]
    P[Photoresistor]
    subgraph Devices
    direction TB
    subgraph  
    
    subgraph Servos
    direction RL
    E-->D
    end
    L
    P
    H
    end
    subgraph Screens
    direction TB
    F---O
    F-->G
    O-->G
    end
    H-->Screens
    subgraph LEDs
    direction TB
    subgraph  
    direction RL
    J---N
    end
    J-->K
    N-->K
    end

end
C-->Devices
L-->LEDs
P-->LEDs
```

<br>
The requirements of the Test Box.

![for Test Box essential and non...](Images/Essential%20and%20Nonessential%20for%20Capstone%20[Test%20Box].jpg)

<br>
The views from different sides of the box. 

![for AI essential and non...](Images/Views%20and%20parts%20of%20the%20Project.jpg)

<br>
The requirements of the AI.

![for AI essential and non...](Images/Essential%20and%20Nonessential%20for%20Capstone%20[AI].jpg)



<br>
<br>

## Parts Tester

<br>
<br>
<br>

### Description
A box that quickly tests certain types of parts

<br>
<br>

### Problems and Solutions


<br>
<br>

### Images progress


<br>
<br>

### Related Links


<br>
<br>


