#include <linux/kernel.h>
#include <linux/module.h>

int init_module(void){
    printk(KERN_INFO "waddup\n");
    return 0;
}

void cleanup_module(void){
    printk(KERN_INFO "peace out\n");
}

MODULE_LICENSE("GPL");
MODULE_AUTHOR("mudbungie");
MODULE_DESCRIPTION("just messin");
MODULE_VERSION("1.0.0");

