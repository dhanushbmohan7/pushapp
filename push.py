from pushbullet import Pushbullet
API_KEY='o.gLR4waT3ey199F4g95g8jJUEtkjbAtkl'
pb=Pushbullet(API_KEY)
text='This is a simple push notificatio'
push=pb.push_note('Important',text)