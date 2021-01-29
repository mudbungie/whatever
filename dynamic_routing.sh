IP1=127.0.0.1 #changeme, was my laptop
IP2=203.0.113.1 #something unroutable from IETF TEST-NET-3, also change
PORT=53535

try_connection(){
    # usage: try_connection target_address target_port
    nc -z -w 1 $1 $2
    return $?
}

forward_port(){
    # usage: forward_port target_address forwarded_port
    echo 1 >/proc/sys/net/ipv4/ip_forward
    iptables -t nat -D PREROUTING -p tcp –dport $2 -j DNAT –to-destination $1
    iptables -t nat -D POSTROUTING -p tcp -d $1 –dport $2 -j MASQUERADE
}

forward_to_working_host(){
    # usage: forward_to_working_host
    if try_connection $IP1 $PORT
    then
        forward_port $IP1 $PORT
        return 0
    elif try_connection $IP2 $PORT
    then
        forward_port $IP1 $PORT
        return 0
    else
        echo "No connections made to $IP1 or $IP2 on $PORT"
        return 1
    fi
}

forward_to_working_host
