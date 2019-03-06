from model3000x2x20482 import model 
import neuthink.metatext as Text 
model.LoadContent(Text.LoadColumn("train.txt")) 
data2 = model.Unroll() 
d=data2.Text.Word2Chunk().model.Parent[0].Exec().DistributeFeatures(source='chunk',target='LSTM3').Child[0].BLSTM(source='LSTM3',target='ttg',size=256).dContextMap(size=256,target='term',source='ttg') 
d.enableGPU('cuda:1') 
model.enableGPU('cuda:1')
f = model.compile(lr=0.0001)
