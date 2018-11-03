from rest_framework import serializers
from .models import Serie

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = ('id_person','name','birthdate','is_admin','mail','phone_number')
    id_person = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    birthdate = serializers.DateTimeField()
    is_admin = serializers.BooleanField()
    mail = serializers.EmailField()
    phone_number = models.CharField()

    def create(self,validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.birthdate=validated_data.get('birthdate',instance.birthdate)
        instance.is_admin= validated_data.get('is_admin',instance.is_admin)
        instance.mail=validated_data.get('mail',instance.mail)
        instance.phone_number =validated_data.get('phone_number',instance.phone_number)
        instance.save()
        return instance

class InstitucionSerializer(serializers.Serializer):
    class Meta:
        model = Institucion
        fields = ('id_institucion','name')
        
    id_institucion = serializers.IntegerField(read_only=True)
    name = serializers.Charfield()

    def create(self,validated_data):
        return Institucion.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance
    
class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = ('id_group','name','members','leader')
        
    id_group = serializers.IntegerField(read_only=True)
    name = serializers.Charfield()
    members = models.Charfield()
    leader = models.

    def create(self, validated_data):
        return Group.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.members = validated_data.get('members',instance.members)
        instance.leader= validated_data.get('leader',instance.leader)
        instance.save()
        return instance

class BranchSerializer(serializers.Serializer):
    class Meta:
        model = Branch
        fields = ('id_branch','id_institucion','name')

    id_branch = serializers.IntegerField(read_only=True)
    id_institucion = serializers.Integerfield()
    name = serializers.Charfield()

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.id_institucion = validated_data('id_institucion',instance.id_institucion)
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance
class  ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ('id_article','title','authors')

    id_article = serializers.IntegerField(read_only=True)
    title  = serializers.Charfield()
    authors = serializers.Charfield()

    def create(self,validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.authors= validated_data.get('authors',instance.authors)
        instance.save()
        return instance
class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Department
        fields = ('id_department','phone_number','direction','id_branch')
        
    id_department = serializers.IntegerField(read_only=True)
    phone_number  = serializers.Charfield()
    direction = serializers.Charfield()
    id_branch = serializers.IntegerField()

    def create(self,validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.phone_number=validated_data.get('phone_number',instance.phone_number)
        instance.direction= validated_data.get('direction',instance.direction)
        instance.save()
        return instance
class InvestigatorSerializer(serializers.Serializer):
    class Meta:
        model = Investigador
        fields = ('id_investigador','id_person','id_department')
        
    id_investigator = serializers.IntegerField(read_only=True)
    id_person = serializers.IntegerField()
    id_department = serializers.IntegerField()

    def create(self,validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_person = validated_data('id_person',instance.id_person)
        instance.id_department = validated_data('id_person',instance.id_department)
        instance.save()
        return instance
    
class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = ('id_student','id_person','id_investigator')

    id_student = serializers.IntegerField(read_only=True)
    id_person = serializers.IntegerField()
    id_investigator = serializers.IntegerField()

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_person = validated_data('id_person',instance.id_person)
        instance.id_investigator = validated_data('id_person',instance.id_investigator)
        instance.save()
        return instance
  
